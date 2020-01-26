import axios from 'axios'

export default {
  fetchData (method, params, data) {
    // if (method === 'get') {
    //   return ajax('api/year/', 'get', null, null)
    // } else {
    //   return ajax('api/year/', 'get', null, null)
    // }

      return ajax('api/year/', 'get', null, null)


  }
}

/**
 *  @param url
 *  @param method
 *  @param params
 *  @param data
 *  @returns
 */

function ajax(url, method, options) {
  if (options !== undefined) {
    var {params = {}, data = {}} = options
  } else {
    params = data = {}
  }

  return new Promise((resolve, reject) => {
    axios({
      url,
      method,
      params,
      data
    }).then(res => {
      resolve(res)
    }, res => {
      reject(res)
    })
  })
}
