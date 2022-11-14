### Add new presentation

- create folder by presentation name, i.e. `{2023}`
  - `mkdir -p 2023`
- add symlink for `reveal.js` for gitlab pages:
  - `ln -rs .contrib/reveal.js/dist 2023/dist`
  - `ln -rs .contrib/reveal.js/plugin 2023/plugin`
- write your `2023/index.html` using documentation for [reveal.js](https://revealjs.com/)
  - I prefer to use [Markdown in html](https://revealjs.com/markdown/)
