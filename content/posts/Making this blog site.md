---
title: Making this blog site
date: 2024-11-13
lastmod: 
draft: false
tags:
  - blog
---

### Introduction

For a while now, I’ve had the idea of wanting to make my own blog site. My main challenges were figuring out where to start, where to host it, or even how to begin writing a blog. I’m no blogger, but here’s my attempt at it.

### Where the Inspiration Came From

After watching this video: [I started a blog.....in 2024 (why you should too)](https://www.youtube.com/watch?v=dnE7c0ELEH8&t=1457s) by NetworkChuck, I decided I could make a blog as well. I followed most of his steps up to the point of pushing the code to GitHub.

### Publishing to GitHub Pages

Since I don’t currently pay for any Virtual Private Server (VPS), I decided to publish my blog using GitHub Pages. I used the workflow provided by the team at Hugo: [workflow script](https://gohugo.io/hosting-and-deployment/hosting-on-github/). The Hugo team outlines a few preparatory steps to ensure the workflow works properly before adding it. Following these steps made deployment straightforward.

### My Current Issue

Everything is working properly, except for one problem: if a post includes an image, the image renders fine when tested locally using:

```bash
hugo server
```
However, once the workflow runs and the site gets published, the images fail to load. Instead, placeholders appear where the image descriptions should be.

This issue persists even though the local setup works perfectly. It seems related to how Hugo or GitHub Pages handles static assets.

### Recommendations

I’m open to recommendations to resolve this issue. If I manage to figure out a solution, I’ll make sure to update this blog post with the fix.

### Conclusion
This project has been a fun experience. It allows me to write blog posts using tools like Obsidian, Notion, or even Neovim (which is my current text editor). Any text editor that supports Markdown works seamlessly, thanks to Hugo. Hugo parses the Markdown files, converts them into valid HTML (HyperText Markup Language), and allows me to publish the site like any regular website using GitHub Pages.