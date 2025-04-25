---
title:
date: 2022-10-24
type: landing

sections:
  - block: resume-biography
    content:
      username: admin
      text:
    design:
      css_class: dark
      background:
        color: black
        image:
          filename: li-yang-5h_dMuX_7RE-unsplash.webp
          filters:
            brightness: 0.4
          size: cover
          position: center
          parallax: false

  - block: markdown
    content:
      title: Scholar Metrics
      text: >
        {{< scholar-metrics >}}
    design:
      columns: '1'

  - block: markdown
    content:
      title: 'Welcome 👋'
      subtitle: ''
      text: |-
        Use this area to speak to your mission. I'm a research scientist in the Moonshot team at DeepMind. I blog about machine learning, deep learning, and moonshots.

        **Specialties:** Analytics & Data, Leadership, Programming, Strategic Planning, Writing & Editing
    design:
      columns: '1'

  - block: collection
    content:
      title: Recent News
      subtitle: ''
      text: ''
      page_type: post
      count: 5
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      offset: 0
      order: desc
    design:
      view: date-title-summary
      spacing:
        padding: [0, 0, 0, 0]
---
