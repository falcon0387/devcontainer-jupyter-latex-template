#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import shutil

# ワークディレクトリ
work_dir = Path(__file__).parent

# 置換対象ファイル
target_file = Path("/home/jovyan/.local/state/crossnote/style.less")

# 置換用ファイル
replacement_file = work_dir / "github_style.less"

# バックアップ保存先ディレクトリ
backup_dir = work_dir / "backup"

# バックアップディレクトリを作成
backup_dir.mkdir(parents=True, exist_ok=True)

# タイムスタンプ生成（YYYYMMDD_HHMMSS）
ts = datetime.now().strftime("%Y%m%d_%H%M%S")

# バックアップ先ファイルパス作成
backup_file = backup_dir / f"{target_file.stem}_{ts}{target_file.suffix}"

# 1. 元ファイルをバックアップ
shutil.copy2(target_file, backup_file)

# 2. 置換用ファイルで上書き
shutil.copy2(replacement_file, target_file)

# 処理完了メッセージの表示
print("Backup and replacement completed successfully.")
