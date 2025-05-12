import json
from pathlib import Path


class UserDataService:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        if not self.file_path.exists():
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            self.file_path.write_text(json.dumps({}, ensure_ascii=False), encoding="utf-8")
        self._load()

    def _load(self):
        try:
            with self.file_path.open("r", encoding="utf-8") as f:
                self.data: dict[str, dict[str, any]] = json.load(f)
        except json.JSONDecodeError:
            self.data = {}

    def _save(self):
        with self.file_path.open("w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def ensure_user(self, user_id: int):
        uid = str(user_id)
        if uid not in self.data:
            self.data[uid] = {"favorites": [], "daily": True}
            self._save()

    # Favorites
    def add_favorite(self, user_id: int, word: str):
        self.ensure_user(user_id)
        favorites = self.data[str(user_id)]["favorites"]
        if word not in favorites:
            favorites.append(word)
            self._save()

    def list_favorites(self, user_id: int) -> list[str]:
        self.ensure_user(user_id)
        return self.data[str(user_id)]["favorites"]

    # Daily
    def enable_daily(self, user_id: int):
        self.ensure_user(user_id)
        if not self.data[str(user_id)]["daily"]:
            self.data[str(user_id)]["daily"] = True
            self._save()

    def disable_daily(self, user_id: int):
        self.ensure_user(user_id)
        if self.data[str(user_id)]["daily"]:
            self.data[str(user_id)]["daily"] = False
            self._save()

    def is_daily_enabled(self, user_id: int) -> bool:
        self.ensure_user(user_id)
        return bool(self.data[str(user_id)]["daily"])

    def list_daily_users(self) -> list[int]:
        return [int(uid) for uid, v in self.data.items() if v.get("daily")]
