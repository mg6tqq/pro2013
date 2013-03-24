# プログラミング入門2013


フォルダ | 内容 
---- | ----
note | 講義ノート (markdown)
workspace | サンプルプログラム (Eclipse workspace)
tools | 整形に使うスクリプトなど
web | webに公開する生成物

----

* 講義ノートはmarkdownで書く
    * エディタ <http://mouapp.com/>
* pandocを使って、HTML、スライド、epubに変換する
    * <http://johnmacfarlane.net/pandoc/>
* プログラムのソースコードはpythonスクリプトでincludeする
    * <http://bricefernandes.com/posts/2011-08-17-pincpy-including-files-and-script-output.html>
* シンタックスハイライトは~~highlight.jsで行う~~ pandocの機能を使う
    * <http://softwaremaniacs.org/soft/highlight/en/>


----
ソースコードのincludeの書き方    

```
全部include
(> ../workspace/project/src/Foo.java <)

5行目から7行目までinclude
(!> sed -n '5,7p' ../workspace/project/src/Foo.java <)
```
