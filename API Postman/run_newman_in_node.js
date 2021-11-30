//код вызова:
//var runNewman = require('./mymodule/run_newman_in_mode');
//var rn = new runNewman(cName, cData);
//var result = rn.run().then(console.log, console.log); //then and catch

var newman = require('newman')

module.exports = function (collection, data) {
  this.run = function () {
    return new Promise((resolve, reject) => {
      newman.run({
        collection: require(this.collection + '.postman_collection.json'),
        environment: require(this.environment + '.postman_environment.json')
      }, function () {
        console.log('in callback')
      }).on('start', function (err, args) {
        if (err) { console.log(err) }
      }).on('beforeDone', function (err, data) {
        if (err) { console.log(err) }
      }).on('done', function (err, summary) {
        if (err) { reject(err) } else { resolve(summary) }
      })
    })
  }
}
