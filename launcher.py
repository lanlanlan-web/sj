from pathlib import Path
import shutil
import sys
import tempfile
import webbrowser


APP_HTML = "身份查询与签到管理系统.html"


def resource_path(name: str) -> Path:
    base_path = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return base_path / name


def main() -> None:
    source = resource_path(APP_HTML)
    target_dir = Path(tempfile.gettempdir()) / "sfzcx_identity_attendance"
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / APP_HTML
    shutil.copy2(source, target)
    webbrowser.open(target.as_uri())


if __name__ == "__main__":
    main()
