# Whatsonmena

## Getting Started

### Installation Instructions

1.  On GitHub, fork the repo by clicking the Fork button in the GitHub UI.
2.  Clone the repo on your local machine and go into the directory:

        $ git clone git@github.com:{YOUR_USERNAME}/whatsonmena.git
        OR
        $ git clone https://github.com/{YOUR_USERNAME}/whatsonmena.git

        $ cd whatsonmena

3.  Add upstream remotes:

        $ git remote add upstream git@github.com:Zarad1993/whatsonmena.git
        OR
        $ git remote add upstream https://github.com/Zarad1993/whatsonmena.git

4.  Create the `web-api-layer` network in Docker (this only needs to happen once):

        $ docker network create web-api-layer

5.  Start up the Vue application web interface container:

    \$ make web

# whatsonmena

## Project setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Run your tests

```
npm run test
```

### Lints and fixes files

```
npm run lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).
