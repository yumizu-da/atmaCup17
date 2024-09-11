# atmaCup#17

<https://www.guruguru.science/competitions/24>

## Branches

- `main`: competition終了後にDisucssionを元に解法をまとめたbranch. 実験結果詳細は`exp/README.md`に記載.
- `ueda`/`nagata`/`mizuta`: 各メンバーの個人branch. 各々の努力の跡を残っています.

## Environment

### dockerコンテナ ビルド & 起動

```bash
docker compose up -d --build
```

## How to use

### 実験方法

1. `exp`以下に`001`, `011`といったようなディレクトリを作成

   - `001`や`011`は実験番号です。このディレクトリ名を読み込んで実験管理を行います

2. `001`以下に全てのコードを管理し、実験を行う

   - 実験結果の再現性を担保するため、1実験1ディレクトリの構成にしています

### uvを用いたライブラリ管理

ライブラリ管理にuvを使用しています. 以下はuvの使用例です

```bash
# ライブラリ追加
uv add pandas
uv add numpy==1.26.4

# ライブラリ削除
uv remove numpy

# pyproject.tomlをもとにパッケージをインストール
uv sync
```
