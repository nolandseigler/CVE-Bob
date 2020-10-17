from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).parent

env_path = project_root / ".env-no-git"

print(f"\nUsing configuration file: '{env_path.resolve()}'")
load_dotenv(dotenv_path=env_path, verbose=True)