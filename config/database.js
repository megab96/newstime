if (process.env.NODE_ENV === 'production'){
    module.exports = { mongoURI: 'mongodb://karl:karl@ds129428.mlab.com:29428/newstime-prd'}
} else {
    module.exports = { mongoURI: 'mongodb://localhost/newstime-dev'}
}