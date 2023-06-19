const { src, dest } = require('gulp');
const fileinclude = require('gulp-file-include');
const rename = require('gulp-rename');
const clean = require('gulp-clean');

exports.default = function() {
  return src('*.md')
        
        .pipe(fileinclude({
            prefix: '@@',
            basepath: '@file',
            context: { arr: ['test1', 'test2'] }
        }))
        .pipe(clean({force: true}))
        .pipe(dest('.'));
}
