const package = require('../package.json');
const fs = require('fs');

const {CODESPACE_NAME = 'test', GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN='test', GITHUB_REPOSITORY='test'} = process.env;

package.scripts["server"] = package.scripts["server"]
    .replace("${CODESPACE_NAME}", CODESPACE_NAME)
    .replace("${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}", GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN);

    fs.writeFileSync('./package.json', JSON.stringify(package, null, 4));

console.log("Injected environment variables into package.json")

var config = fs.readFileSync('./static/admin/config.yml', 'utf8')

config = config
    .replace("${GITHUB_REPOSITORY}", GITHUB_REPOSITORY)
    .replace("${CODESPACE_NAME}", CODESPACE_NAME)
    .replace("${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}", GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN);

    fs.writeFileSync('./static/admin/config.yml', config);

console.log("Injected environment variables into Decap CMS config.yml")