import {request} from './request'

export function getHomePosts(page) {
    return request({
        url: 'home/posts/',
        params:{
            page
        }
    })
}