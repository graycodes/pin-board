'use strict';


var updateMail = function() {
    var python = require('child_process').spawn(
        'python',
        ['lib/mail.py']
    );

    python.stdout.on('data', function(data){ 
        console.log('data: ' + new Buffer(data, 'hex').toString());
    });

    python.stderr.on('data', function(data){ 
        console.log('err: ' + new Buffer(data, 'hex').toString());
    });

    python.on('close', function(code){ 
        return console.log(500, code); 
    });

    console.log('updated');
};
setInterval(updateMail, 60000);
updateMail();
