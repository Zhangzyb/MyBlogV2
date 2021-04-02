import { request } from './request'

export function getTimeData() {
    return request({
        url: 'time/'
    })
}