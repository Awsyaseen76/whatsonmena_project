module.exports = {
  rules: {
    'no-console': 'off'
  },
  extends: 'plugin:vue/base',
  parser: 'vue-eslint-parser',
  parserOptions: {
    parser: 'babel-eslint',
    sourceType: 'module'
  },
  plugins: ['@vue']
};
