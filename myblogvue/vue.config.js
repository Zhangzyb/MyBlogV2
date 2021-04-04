const path = require('path');
function resolve(dir) {
    return path.join(__dirname, dir)
}


module.exports = {
    publicPath: "./",
    assetsDir: "static",
    chainWebpack: (config) => {
        config.resolve.alias
            .set('@', resolve('./src'))
            .set('components', resolve('./src/components'))
            .set('assets', resolve('./src/assets'))
            .set('views', resolve('./src/views'))
            .set('network', resolve('./src/network'))
    }
}