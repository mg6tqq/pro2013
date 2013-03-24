python ../tools/pinc.py < 01-note.md | \
pandoc --toc \
    --self-contained \
    --to=html5 \
    --highlight-style=pygments \
    --include-in-header=header.html \
    -o ../web/01.html

#pygments
#kate
#monochrome
#espresso
#zenburn
#haddock
#tango
