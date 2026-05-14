from pathlib import Path
import os
import shutil
import sys
import tempfile
import tkinter.messagebox as messagebox


APP_HTML = "身份查询与签到管理系统.html"


def resource_path(name: str) -> Path:
    base_path = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return base_path / name


def main() -> None:
    try:
        source = resource_path(APP_HTML)
        target_dir = Path(tempfile.gettempdir()) / "sfzcx_identity_attendance"
        target_dir.mkdir(parents=True, exist_ok=True)
        target = target_dir / APP_HTML
        shutil.copy2(source, target)
        os.startfile(str(target))
    except Exception as exc:
        messagebox.showerror("启动失败", f"无法打开系统页面：\n{exc}")


if __name__ == "__main__":
    main()
