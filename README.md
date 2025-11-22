# Python Minimal Starter (pyenv + Poetry)

Windowsを前提とした、pyenv-win と Poetry を使う最小構成の Python 開発環境テンプレートです。

## セットアップ

### 1) pyenv-win のインストール（未導入なら）
インストールコマンド

```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```
```powershell
.\install-pyenv-win.ps1
```
```powershell
$env:PYENV="$env:USERPROFILE\.pyenv\pyenv-win\"
$env:PYENV_ROOT=$env:PYENV
$env:PYENV_HOME=$env:PYENV
$env:PATH="$env:USERPROFILE\.pyenv\pyenv-win\bin;$env:USERPROFILE\.pyenv\pyenv-win\shims;$env:PATH"
```


### 2) Python のインストール（pyenv） バージョン切り替え可能

- インストール可能なバージョン一覧の確認:
  ```powershell
  pyenv install --list
  ```
- 例: Python 3.12.5 を入れる:
  ```powershell
  pyenv install 3.12.5
  ```
- インストール済みバージョンの確認:
  ```powershell
  pyenv versions
  ```

#### pyenv: global と local の違い

- global: ユーザー全体のデフォルト設定。プロジェクト外で使う Python を切り替える。
  ```powershell
  pyenv global 3.12.5
  ```
- local: 現在のディレクトリ（＝このプロジェクト）に対する設定。`.python-version` を作成し、以後このプロジェクトではその Python を優先使用する。`.python-version` は Git にコミット推奨。
  ```powershell
  pyenv local 3.12.5
  ```
- 優先度: `local > global > system`
- 確認コマンド:
  ```powershell
  pyenv version    # 現在有効な 1 つ
  pyenv versions   # インストール済み一覧（* が現在有効）
  ```

### 3) Poetry のインストール（未導入なら）

- 公式手順: https://python-poetry.org/docs/#installing-with-the-official-installer
- インストールコマンド
  ```powershell
  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
  ```
- 環境変数 PATH に `%APPDATA%\Python\Scripts` を追加。
- バージョン確認:
  ```powershell
  poetry -v
  ```

### 4) 仮想環境の作成と依存インストール

- 仮想環境作成（`.venv/` を作る）と依存インストール（`pyproject.toml` に基づく）
  ```powershell
  poetry install
  ```

### 5) 動作確認

- テスト実行:
  ```powershell
  poetry run pytest
  ```
- サンプル実行:
  ```powershell
  poetry run python -c "from app.hello import hi; print(hi('world'))"
  ```

## 依存関係の追加（バージョン指定を含む）

- 通常追加:
  ```powershell
  poetry add requests
  ```
- バージョン指定の例:
  ```powershell
  poetry add requests@^2.32         # 互換範囲（^2.32 = >=2.32,<3.0）
  poetry add requests@~2.32.0       # マイナー固定（~2.32.0 = >=2.32.0,<2.33.0）
  poetry add requests==2.32.3       # 完全固定
  poetry add "requests>=2.32,<3.0"   # 範囲を直接指定
  ```
- 開発用依存（dev）として追加:
  ```powershell
  poetry add -D black@24.8.0 isort@5.13.2 pytest@^8.3
  ```
- 依存の更新/削除:
  ```powershell
  poetry update           # すべて更新
  poetry update requests  # 指定パッケージのみ更新
  poetry remove requests  # 削除
  ```

## プロジェクト構成とファイルの説明

```
python-starter/
├─ pyproject.toml
├─ poetry.toml
├─ .python-version
├─ .gitignore
├─ src/
│  └─ app/
│     ├─ __init__.py
│     └─ hello.py
├─ tests/
│  └─ test_hello.py
└─ (生成物) .venv/, poetry.lock
```

- pyproject.toml: プロジェクト名/バージョン/依存など、必要なパッケージの定義と設定を記述。
- poetry.lock: 実際に解決・インストールされたパッケージと厳密なバージョンを固定。初回 `poetry install` や `poetry add` で生成/更新される。チームで同一環境を再現するためにコミット推奨。
- poetry.toml: Poetry のローカル設定。本テンプレートでは仮想環境をプロジェクト直下に作る `virtualenvs.in-project = true` を設定。
- .python-version: このプロジェクトで使用する Python バージョン（pyenv の local 設定）。
- src/app: アプリケーション本体のパッケージ配置場所。
- tests: pytest のテスト配置場所。
- .venv: Poetry が作成する仮想環境ディレクトリ（`virtualenvs.in-project = true` 時に生成）。

## よく使うコマンド

- 仮想環境へ入る/出る: `poetry shell` / `exit`
- フォーマット: `poetry run black .`
- インポート整形: `poetry run isort .`
- テスト: `poetry run pytest`
- スクリプト実行: `poetry run python your_script.py`
