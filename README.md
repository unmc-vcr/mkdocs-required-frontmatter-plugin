# Required Frontmatter for MkDocs

[MkDocs](https://www.mkdocs.org/) allows arbitrary YAML frontmatter in markdown documents. This plugin enforces arbitrary required frontmatter for pages in the documentation pages.  This may be especially useful if you have post-processing scripts that rely on certain frontmatter existing in your documents.

## Setup

Install the plugin using pip3 with the following command:

pip3 install mkdocs-required-frontmatter-plugin

Next, in your mkdocs.yml, add the following lines:

``` yaml
plugins:
    - required-frontmatter
```

## Configuration Options

`enabled` allows you to disable the plugin, for instace in different build environments that shouldn't require it.

``` yaml
plugins:
    - required-frontmatter
        enabled: true
```

`required_keys` specifies the frontmatter keys that the plugin will search for on all documents.

``` yaml
plugins:
    - required-frontmatter
        required_keys:
            - title
            - author
            - description
```

`exclude` is a list of files or directories in the `/docs` folder that this plugin will ignore.  It accepts exact paths and glob-style strings to ignore entire directories or file types.

``` yaml
plugins:
    - required-frontmatter
        exclude:
            - index.md
            - folder/*
```

`strict` defines whether the plugin will raise an error and fail to build (default) or issue a warning when the required frontmatter is not present.

``` yaml
plugins:
    - required-frontmatter
        strict: true
```


