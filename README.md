### Index

- [Know Your ClickHouse](2022-know-your-clickhouse)

### Add new presentation

- create folder by presentation name, i.e. `{2023}`
  - `mkdir -p 2023`
- add symlink for `reveal.js` for gitlab pages:
  - `ln -rs .contrib/reveal.js/dist 2023/dist`
  - `ln -rs .contrib/reveal.js/plugin 2023/plugin`
- write your `2023/index.html` using documentation for [reveal.js](https://revealjs.com/)
  - I prefer to use [Markdown in html](https://revealjs.com/markdown/)

### Converting to PDF

All you need is to add `?print-pdf` to the URL, i.e.:

    https://azat.sh/presentations/2022-know-your-clickhouse/?print-pdf

For more details you can see the [official documentation](https://revealjs.com/pdf-export/).
