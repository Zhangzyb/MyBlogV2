import {request} from './request'

export function getDynamic(){
    return request({
        url: 'dynamic/'
    })
}