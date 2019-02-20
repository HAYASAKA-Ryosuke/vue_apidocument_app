module.exports = {
  root: false,
  env: {
    browser: false,
    node: false 
  },
  parserOptions: {
    parser: 'babel-eslint'
  },
  extends: [
    '@nuxtjs',
    //'plugin:vue/recommended'
  ],
  plugins: [
    //'prettier'
		//'vue'
  ],
  // add your custom rules here
  rules: {}
}
