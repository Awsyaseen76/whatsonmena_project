# Vue

## Start from 0:

`npm install -g @vue/cli`

<!-- `npm install -g @aws-amplify/cli` -->

### Create a App:

- `vue create whatsonmena`
- Choose: Babel, Router, Vuex and Linter/Formatter
  the configurations for babel, eslint ... is in the package.json
- run the app
  `npm run serve`

#### The power of Prettier:

- config Prettier in package.json
  using single quote and tab 4 spaces not 2(default)
- put it in action from terminal:
  `npm run lint`

## Using Vuetify:

- `vue add vuetify`

## Try to put it on Docker

- create the Dockerfile
- terminal:
    <!-- `docker build -t dockerize-vue .` -->
  `docker build -t auth-vue .`
  run it:
  1. the normal will run on the port 8080
     `docker run -it -p 8080:80 --rm --name dockerize-vuejs dockerize-vue`
     go to:
     `localhost:8080`
  2. to use the updated version that get data from django change the port to 4200 as what heppend on the file vue.config.js
     `docker run -it -p 4200:80 --rm --name dockerize-vuejs dockerize-vue`
     now go to:
     `localhost:4200`

###Notes:

1. if go to: `localhost:8080/home` (with home) it is not working
   but if we use the navbar its ok (without home)
2. the menu bar for the larg screen is not ok

## Connect to Django:

- `npm install axios`
- create the file glue.js it will glue the vue with the django:
  import axios
  create axios and set the base url 'http://localhost:8000/auth_api'
- on the file vue.config.js:
  Set the port for 4200 that match the port on CORS settings in django in the CORS_ORIGIN_WHITELIST

---

---

---

---

---

---

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
