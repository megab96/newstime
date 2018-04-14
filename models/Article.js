const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Create Schema
const ArticleSchema = new Schema({
    title: {
        type: String,
        required: true
    },
    link: {
        type: String,
        required: true
    },
    // story: {
    //     type: Schema.Types.ObjectId, ref: 'Story'
    // },
    date_added: {
        type: Date,
        default: Date.now
    }

});

const Article = mongoose.model('articles', ArticleSchema)