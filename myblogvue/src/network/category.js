import {request} from './request'

export function getCategory(){
    return request({
        url:'category/'
    })
}