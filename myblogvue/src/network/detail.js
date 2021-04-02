import { request } from './request'

export function getDetail(id) {
    return request({
        url: 'home/posts/' + id + '/'
    })
}

export function getComments(article) {
    return request({
        url: 'comments/',
        params: {
            article: article
        }
    })
}

export function postComment(data) {
    return request({
        url: 'comments/',
        method: 'post',
        data: data
    })
}

export function getSubComment(id) {
    return request({
        url: 'comments/',
        params: {
            comment_id: id
        }
    })
}

export function addAgree(id, data) {
    return request({
        url: 'comments/' + id + '/',
        method: 'patch',
        data: data
    })
}