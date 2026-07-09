#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
FORCE=0
PRUNE=0
REFRESH=0

usage() {
  cat <<'EOF'
Usage: setup_codex_skills.sh [--target DIR] [--force] [--prune] [--refresh]

Create symlinks for all top-level skill folders in this repo into the
Codex skills directory.

Options:
  --target DIR  Override the target skills directory
  --force       Replace existing symlinks that point elsewhere
  --prune       Remove symlinks in target that no longer exist in repo
  --refresh     Equivalent to --force --prune
  -h, --help    Show this help
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      shift
      if [[ $# -eq 0 ]]; then
        echo "Missing value for --target" >&2
        exit 1
      fi
      TARGET_DIR="$1"
      ;;
    --force)
      FORCE=1
      ;;
    --prune)
      PRUNE=1
      ;;
    --refresh)
      REFRESH=1
      FORCE=1
      PRUNE=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
  shift
done

mkdir -p "$TARGET_DIR"

declare -A REPO_SKILLS=()

link_skill() {
  local skill_dir="$1"
  local skill_name
  skill_name="$(basename "$skill_dir")"
  REPO_SKILLS["$skill_name"]=1
  local target_link="$TARGET_DIR/$skill_name"

  if [[ -L "$target_link" ]]; then
    local current_target
    current_target="$(readlink "$target_link")"
    if [[ "$current_target" == "$skill_dir" ]]; then
      echo "OK  $skill_name -> $current_target"
      return 0
    fi

    if [[ "$FORCE" -eq 1 ]]; then
      rm "$target_link"
    else
      echo "SKIP $skill_name (already linked to $current_target)" >&2
      return 0
    fi
  elif [[ -e "$target_link" ]]; then
    echo "SKIP $skill_name (path exists and is not a symlink): $target_link" >&2
    return 1
  fi

  ln -s "$skill_dir" "$target_link"
  echo "LINK $skill_name -> $skill_dir"
}

for skill_dir in "$ROOT_DIR"/*; do
  [[ -d "$skill_dir" ]] || continue
  [[ -f "$skill_dir/SKILL.md" ]] || continue
  link_skill "$skill_dir"
done

if [[ "$PRUNE" -eq 1 ]]; then
  for target_link in "$TARGET_DIR"/*; do
    [[ -L "$target_link" ]] || continue
    local_name="$(basename "$target_link")"
    if [[ -z "${REPO_SKILLS[$local_name]+x}" ]]; then
      rm "$target_link"
      echo "PRUNE $local_name"
    fi
  done
fi

echo "Done. Skills linked into: $TARGET_DIR"
