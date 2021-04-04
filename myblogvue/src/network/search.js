import { request } from './request'

export function getSearchResult(query) {
    return request({
        url: 'search/',
        params: {
            text: query
        }
    })
}