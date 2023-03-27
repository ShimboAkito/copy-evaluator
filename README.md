# copy-evaluator
東京コピーライターズクラブさんが提供しているコピラからキャッチコピーを収集するツールを公開しています

## 使い方
`makedataset.sh`を実行します。
例)
```bash makedataset.sh```

`./data/`以下に`slogans.tsv`,`balanced_dataset/`, `full_dataset/`が作られるはずです。

`data/balanced_dataset/`, `data/full_dataset/`の下にさらに`copyonly`, `sector`, `company`, `sector_company`というフォルダが作らます。
業種や企業名を入力として使うのでなければ`copyonly`を使えば十分です。

## Reference

```
@InProceedings{Copira_dataset,
  author = 	"新保彰人 and 山田寛章 and 徳永健伸",
  title = 	"参照例を使わないキャッチコピーの自動評価",
  booktitle = 	"言語処理学会第29回年次大会",
  year =	"2023",
  url = "https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/A7-2.pdf"
  note= "in Japanese"
}
```