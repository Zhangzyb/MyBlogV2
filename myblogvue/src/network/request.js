import axios from 'axios'
import store from '../store/index'

export function request(config){
    const instance = axios.create({
        baseURL: 'http://127.0.0.1:8000/api/v1/blog',
        timeout: 5000
    })
    return instance(config)
}