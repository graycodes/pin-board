'use strict';


var updateMail = function() {
    var python = require('child_process').spawn(
        'python',
        ['mail.py']
    );

     python.stdout.on('data', function(data){ console.log(data); });
     python.on('close', function(code){ 
         return console.log(500, code); 
     });
    console.log('updated');
};
setInterval(updateMail, 60000);
updateMail();
