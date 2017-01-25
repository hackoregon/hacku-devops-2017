## Assignment 2 - Create Continuous Integration Environment

### Prerequsites
- Student has Github account
- Student has Node JS installed on local laptop

### Concepts Introduced
- Continuous Build
- Continuous Integration
- Working with AWS CLI
- Test Driven Development (TDD)

### Step 1 - Fork and clone sample project
- First browse to this project and hit the Fork button to create your own (writeable) copy of the project: https://github.com/hackoregon/programmingforprogress-frontend.git
- Then click the *Clone or download* button (at the far right) and then the Copy button to get the URL for the project, so you can clone *your* copy
- You'll run commands like this (but substituting the URL of your project instead)
```bash
$ git clone https://github.com/YOURGITHUBUSERNAME/programmingforprogress-frontend.git
```
### Step 2 - Setup Travis/GitHub integration
1. Log in to http://travis-ci.org using your github credentials
2. Add your repository
3. Activate the repository **<github user name>/programmingforprogress-frontend**

Note: if the setup/welcome page doesn't redirect you after five minutes, just browse to your Accounts page (https://travis-ci.org/profile/) to activate the repository

### Step 3 - Install local travis client and login using github credentials
```bash 
$ sudo gem install travis
$ travis login --auto
```
### Step 4 - AWS Configuration
1. [Do Steps 1-3 in AWS tutorial to setup bucket policy](http://docs.aws.amazon.com/gettingstarted/latest/swh/setting-up.html)
2. [Follow the instructions to create your AWS CLI credentials](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html)

### Step 5 - Configure Travis build config file replacing with your AWS key id
Create .travis.yml file and save to project directory
```yaml
language: node_js
node_js:
- '6.0'
install: npm install
deploy:
  provider: s3
  access_key_id: <access_key_id>
  bucket: <bucket_name>
  region: us-west-2
```
We need to encrypt the our secret access key. Do not store your AWS credentials in your repository. From the command line:

```bash
$ travis encrypt --add deploy.secret_access_key 
```
When prompted enter your AWS Secret key

### Step 5 - Push changes & check build
```bash
$ git add .
$ git commit . -m "added travis configuration"
```
Browse to your travis home page (https://travis-ci.org/) and watch the build. It will fail.

### Step 6 - Install Mocha & Setup Tests

Add the following line to your .travis.yml file before the **install:** line to install the mocha framework

`
before_install: npm install mocha
`

From your local command line:
```bash
$ npm install mocha
```

Edit package.json file in project directory to this:
```javascript
"scripts": {
  "test":"mocha",
```

create a stubbed unit test function

```bash
$ mkdir test
```
in your favorite editor create the file test/test.js with the following:

```javascript
var assert = require('assert');
describe('Array', function() {
  describe('#indexOf()', function() {
    it('should return -1 when the value is not present', function() {
      assert.equal(-1, [1,2,3].indexOf(4));
    });
  });
});
```

from your command line run:

```bash
$ npm test
```

You should see:
```bash
Array
  #indexOf()
    ✓ should return -1 when the value is not present

1 passing (12ms)
```

Commit your changes from the command line

```bash
$ git add .
$ git commit . -m "added first test"
```

Switch to travis page and watch build. It should pass.
