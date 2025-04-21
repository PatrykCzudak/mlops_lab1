import os
import yaml
import argparse
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_files = {"dev": ".env.dev", "test": ".env.test", "prod": ".env.prod"}

    if environment not in env_files:
        raise ValueError(
            f"""Invalid environment: {environment}.
            Must be one of {", ".join(env_files.keys())}."""
        )

    env_file = env_files[environment]
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"{env_file} not found.")

    load_dotenv(env_file)
    print(f"Loaded environment variables from {env_file}")
    
    secrets_path = "secrets.yaml"
    if os.path.exists(secrets_path):
        with open(secrets_path, "r") as f:
            data = yaml.safe_load(f) or {}
        for k, v in data.items():
            os.environ.setdefault(k.upper(), str(v))
        print(f"Loaded secrets from {secrets_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("DATABASE_PASSWORD:", settings.DATABASE_PASSWORD)
    print("API_KEY:", settings.API_KEY)
