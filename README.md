# copy-evaluator
東京コピーライターズクラブさんが提供しているコピラからキャッチコピーを収集するツールを公開しています

## 使い方
`makedataset.sh`を実行します。
例)
```bash makedataset.sh```

`./data/`以下に`slogans.tsv`,`balanced_dataset/`, `full_dataset/`が作られるはずです。

`data/balanced_dataset/`, `data/full_dataset/`の下にさらに`copyonly`, `sector`, `company`, `sector_company`というフォルダが作らます。
業種や企業名を入力として使うのでなければ`copyonly`を使えば十分です。

