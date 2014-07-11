'use strict';

setInterval(function() {
    var python = require('child_process').spawn(
        'python',
        ['mail.py']
    );
    console.log(python);
    console.log('updated');
}, 60000);
