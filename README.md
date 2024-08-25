# atmaCup#17

<https://www.guruguru.science/competitions/24>

## Environment

### dockerコンテナ ビルド & 起動

```bash
docker compose up -d --build
```

### コンテナにアタッチ

次にVScode左下の`><`ボタンより`コンテナで再度開く`でコンテナにアクセス

### 拡張機能インストール

無事コンテナが開いたら, 「拡張機能の推奨事項があります」という通知が出ると思います.
この通知を許可すると, `.vscode/extensions.json`に記載されている拡張機能が自動的にインストールされます.
もし通知が出なかった場合は, 左のメニューから`拡張機能`を選択し, `フィルターアイコン`->`推奨`‐>`インストールアイコン`を押せば一括インストールできます.

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
