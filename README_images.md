# 画像ファイルのコピー方法

画像ファイルを`images`フォルダにコピーするには、以下のいずれかの方法を使用してください。

## 方法1: バッチファイルを使用
`copy_images_simple.bat`をダブルクリックして実行してください。

## 方法2: 手動でコピー
1. ファイルエクスプローラーで`2025素材\2025素材\`フォルダを開く
2. すべての`.jpg`ファイルと`.mp4`ファイルを選択（Ctrl+A）
3. `images\`フォルダにコピー（Ctrl+C → imagesフォルダでCtrl+V）

## 方法3: PowerShellコマンド
```powershell
Get-ChildItem -Path "2025素材\2025素材" -Filter "*.jpg" | Copy-Item -Destination "images\" -Force
Get-ChildItem -Path "2025素材\2025素材" -Filter "*.mp4" | Copy-Item -Destination "images\" -Force
```

画像をコピーした後、以下のコマンドでGitに追加・コミット・プッシュしてください：

```bash
git add images/
git commit -m "Add image files"
git push origin main
```

