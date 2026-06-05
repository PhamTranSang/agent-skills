#!/usr/bin/env python3
"""Generate a concise per-repository Codex project context file."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
from typing import Iterable


EXCLUDED_DIRS = {
    ".git",
    ".gradle",
    ".idea",
    ".mvn",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "out",
    "target",
    "venv",
}

BUILD_FILES = {
    "build.gradle": "Gradle",
    "build.gradle.kts": "Gradle Kotlin DSL",
    "pom.xml": "Maven",
    "settings.gradle": "Gradle settings",
    "settings.gradle.kts": "Gradle Kotlin settings",
    "package.json": "Node/npm",
    "pnpm-lock.yaml": "pnpm",
    "yarn.lock": "Yarn",
    "Cargo.toml": "Cargo/Rust",
    "go.mod": "Go modules",
    "pyproject.toml": "Python",
    "requirements.txt": "Python requirements",
    "Gemfile": "Ruby",
    "composer.json": "PHP Composer",
    "next.config.js": "Next.js config",
    "next.config.mjs": "Next.js config",
    "next.config.ts": "Next.js config",
    "vite.config.js": "Vite config",
    "vite.config.mjs": "Vite config",
    "vite.config.ts": "Vite config",
    "tsconfig.json": "TypeScript config",
}

LANGUAGE_EXTENSIONS = {
    ".java": "Java",
    ".kt": "Kotlin",
    ".js": "JavaScript",
    ".jsx": "JavaScript/React",
    ".ts": "TypeScript",
    ".tsx": "TypeScript/React",
    ".py": "Python",
    ".go": "Go",
    ".rs": "Rust",
    ".rb": "Ruby",
    ".php": "PHP",
    ".cs": "C#",
    ".swift": "Swift",
}

FRAMEWORK_PACKAGES = {
    "@angular/core": "Angular",
    "@nestjs/core": "NestJS",
    "@remix-run/react": "Remix",
    "@sveltejs/kit": "SvelteKit",
    "astro": "Astro",
    "express": "Express",
    "fastify": "Fastify",
    "hono": "Hono",
    "next": "Next.js",
    "react": "React",
    "svelte": "Svelte",
    "vue": "Vue",
}


def iter_files(root: Path, max_files: int) -> Iterable[Path]:
    count = 0
    for current_root, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDED_DIRS)
        for name in sorted(files):
            path = Path(current_root) / name
            if path.name == ".DS_Store":
                continue
            yield path
            count += 1
            if count >= max_files:
                return


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def detect_languages(files: list[Path]) -> list[str]:
    languages: dict[str, int] = {}
    for path in files:
        language = LANGUAGE_EXTENSIONS.get(path.suffix)
        if language:
            languages[language] = languages.get(language, 0) + 1
    return [f"{name} ({count})" for name, count in sorted(languages.items())]


def detect_build_files(root: Path) -> list[str]:
    found = []
    for file_name, label in BUILD_FILES.items():
        path = root / file_name
        if path.exists():
            found.append(f"- `{file_name}`: {label}")
    return found


def read_package_json(root: Path) -> dict:
    package_json = root / "package.json"
    if not package_json.exists():
        return {}
    try:
        return json.loads(package_json.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def detect_package_manager(root: Path, package_json: dict) -> str | None:
    package_manager = package_json.get("packageManager")
    if isinstance(package_manager, str) and package_manager:
        return package_manager
    if (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (root / "yarn.lock").exists():
        return "yarn"
    if (root / "package-lock.json").exists():
        return "npm"
    if (root / "bun.lockb").exists() or (root / "bun.lock").exists():
        return "bun"
    if package_json:
        return "npm"
    if (root / "gradlew").exists():
        return "Gradle wrapper"
    if (root / "build.gradle").exists() or (root / "build.gradle.kts").exists():
        return "Gradle"
    if (root / "mvnw").exists():
        return "Maven wrapper"
    if (root / "pom.xml").exists():
        return "Maven"
    if (root / "Cargo.toml").exists():
        return "Cargo"
    if (root / "go.mod").exists():
        return "Go modules"
    if (root / "pyproject.toml").exists():
        return "Python/pyproject"
    return None


def detect_frameworks(root: Path, package_json: dict) -> list[str]:
    frameworks = set()
    deps = {}
    for key in ("dependencies", "devDependencies", "peerDependencies"):
        value = package_json.get(key)
        if isinstance(value, dict):
            deps.update(value)
    for package_name, label in FRAMEWORK_PACKAGES.items():
        if package_name in deps:
            frameworks.add(label)
    if any((root / name).exists() for name in ("next.config.js", "next.config.mjs", "next.config.ts")):
        frameworks.add("Next.js")
    if any((root / name).exists() for name in ("vite.config.js", "vite.config.mjs", "vite.config.ts")):
        frameworks.add("Vite")
    if (root / "go.mod").exists():
        frameworks.add("Go modules")
    if (root / "Cargo.toml").exists():
        frameworks.add("Cargo/Rust")
    if (root / "pom.xml").exists():
        frameworks.add("Maven")
    if (root / "build.gradle").exists() or (root / "build.gradle.kts").exists():
        frameworks.add("Gradle")
    return sorted(frameworks)


def collect_dirs(root: Path, limit: int) -> list[str]:
    dirs = []
    for current_root, child_dirs, _ in os.walk(root):
        child_dirs[:] = sorted(d for d in child_dirs if d not in EXCLUDED_DIRS)
        current = Path(current_root)
        if current == root:
            continue
        dirs.append(rel(current, root))
        if len(dirs) >= limit:
            break
    return dirs


def command_hints(root: Path, package_json: dict) -> list[str]:
    hints = []
    if (root / "gradlew").exists():
        hints.extend(["- Build/test: `./gradlew test`", "- Full build: `./gradlew build`"])
    elif (root / "build.gradle").exists() or (root / "build.gradle.kts").exists():
        hints.extend(["- Build/test: `gradle test`", "- Full build: `gradle build`"])
    if (root / "mvnw").exists():
        hints.extend(["- Maven test: `./mvnw test`", "- Maven package: `./mvnw package`"])
    elif (root / "pom.xml").exists():
        hints.extend(["- Maven test: `mvn test`", "- Maven package: `mvn package`"])
    if (root / "package.json").exists():
        manager = detect_package_manager(root, package_json) or "npm"
        runner = "npm run"
        if manager.startswith("pnpm"):
            runner = "pnpm"
        elif manager.startswith("yarn"):
            runner = "yarn"
        elif manager.startswith("bun"):
            runner = "bun run"
        scripts = package_json.get("scripts") if package_json else None
        if isinstance(scripts, dict) and scripts:
            for script_name in ("dev", "build", "test", "lint", "typecheck", "check", "start"):
                if script_name in scripts:
                    hints.append(f"- Node `{script_name}`: `{runner} {script_name}`")
        else:
            hints.append("- Node scripts: inspect `package.json` before running commands")
    if (root / "Cargo.toml").exists():
        hints.append("- Rust test: `cargo test`")
    if (root / "go.mod").exists():
        hints.append("- Go test: `go test ./...`")
    if (root / "pyproject.toml").exists() or (root / "requirements.txt").exists():
        hints.append("- Python tests: inspect project config for pytest/unittest command")
    return hints


def important_files(root: Path, files: list[Path], limit: int) -> list[str]:
    names = {
        "README.md",
        "README",
        "module-info.java",
        "package.json",
        "pyproject.toml",
        "Cargo.toml",
        "go.mod",
        "pom.xml",
        "build.gradle",
        "build.gradle.kts",
        "settings.gradle",
        "settings.gradle.kts",
        "next.config.js",
        "next.config.mjs",
        "next.config.ts",
        "vite.config.js",
        "vite.config.mjs",
        "vite.config.ts",
        "tsconfig.json",
        "eslint.config.js",
        "eslint.config.mjs",
    }
    selected = [path for path in files if path.name in names]
    return [f"- `{rel(path, root)}`" for path in selected[:limit]]


def render(root: Path, files: list[Path], max_dirs: int, declared_stack: str | None) -> str:
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    dirs = collect_dirs(root, max_dirs)
    languages = detect_languages(files)
    package_json = read_package_json(root)
    package_manager = detect_package_manager(root, package_json)
    frameworks = detect_frameworks(root, package_json)
    build_files = detect_build_files(root)
    hints = command_hints(root, package_json)
    important = important_files(root, files, 40)

    return "\n".join(
        [
            "# Project Context",
            "",
            f"- Last refreshed: `{now}`",
            f"- Repository root: `{root}`",
            "",
            "## Purpose",
            "",
            "- TODO: Summarize what this project does and who it is for.",
            "",
            "## Stack",
            "",
            f"- User-declared stack: {declared_stack or 'not provided'}",
            f"- Languages detected: {', '.join(languages) if languages else 'TODO'}",
            f"- Package/build manager: {package_manager or 'TODO'}",
            f"- Frameworks/tools detected: {', '.join(frameworks) if frameworks else 'TODO'}",
            "",
            "## Build And Config Files",
            "",
            *(build_files or ["- TODO: Add build/config files."]),
            "",
            "## Important Files",
            "",
            *(important or ["- TODO: Add important files."]),
            "",
            "## Source Layout",
            "",
            *(f"- `{directory}/`" for directory in dirs),
            "",
            "## Commands",
            "",
            *(hints or ["- TODO: Add build/test/run commands that actually work."]),
            "",
            "## Architecture Notes",
            "",
            "- TODO: Add package/module responsibilities and public API entry points.",
            "",
            "## Conventions",
            "",
            "- TODO: Add naming, testing, error handling, formatting, and dependency conventions.",
            "",
            "## Risks And Invariants",
            "",
            "- TODO: Add security, correctness, compatibility, or migration constraints.",
            "",
            "## Current Roadmap Notes",
            "",
            "- TODO: Add durable status notes only. Remove stale notes aggressively.",
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_path", nargs="?", help="Repository root")
    parser.add_argument("--root", default=None, help="Repository root; kept for backward compatibility")
    parser.add_argument("--stack", "--language", dest="stack", default=None, help="User-declared project language or stack")
    parser.add_argument("--output", default=None, help="Output markdown path")
    parser.add_argument("--max-files", type=int, default=5000)
    parser.add_argument("--max-dirs", type=int, default=120)
    args = parser.parse_args()

    root_arg = args.project_path or args.root or "."
    root = Path(root_arg).resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Root is not a directory: {root}")

    files = list(iter_files(root, args.max_files))
    output = Path(args.output).resolve() if args.output else root / ".codex" / "project-context.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(root, files, args.max_dirs, args.stack), encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
