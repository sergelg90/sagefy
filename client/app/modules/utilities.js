/*
Utilities are one-off functions that are used throughout the framework.
*/
const util = {}

// Test for types.
;[
    'Object',
    'Array',
    'Function',
    'Date',
    'String',
    'RegExp'
].forEach((type) => {
    util['is' + type] = (a) => {
        return Object.prototype.toString.call(a) === '[object ' + type + ']'
    }
})

util.isUndefined = (a) => {
    return typeof a === 'undefined'
}

const objectConstructor = {}.constructor

// Add the properties of the injects into the target.
util.extend = (target, ...injects) => {
    injects.forEach(inject => {
        Object.keys(inject).forEach(prop => {
            const val = inject[prop]
            if(util.isUndefined(val)) { return }
            if(util.isDate(val)) {
                target[prop] = new Date(val)
            } else if (util.isArray(val)) {
                if(!util.isArray(target[prop])) { target[prop] = [] }
                target[prop] = util.extend([], target[prop], val)
            } else if (util.isObject(val) &&
                       val.constructor === objectConstructor) {
                if(!util.isObject(target[prop])) { target[prop] = {} }
                target[prop] = util.extend({}, target[prop], val)
            } else {
                target[prop] = val
                // number, boolean, string, regexp, null, function
            }
        })
    })
    return target
}

// Makes a copy of the array or object.
util.copy = (obj) => {
    if (util.isObject(obj)) {
        return util.extend({}, obj)
    }
    if (util.isArray(obj)) {
        return util.extend([], obj)
    }
    if (util.isDate(obj)) {
        return new Date(obj)
    }
    return obj
}

// Try to parse a string as JSON, otherwise just return the string.
util.parseJSON = (str) => {
    try {
        return JSON.parse(str)
    } catch (e) {
        return str
    }
}

// Find the closest element matching the given selector.
require('./matches_polyfill')

util.closest = (element, selector, top = document.body) => {
    while (!element.matches(selector)) {
        element = element.parentNode
        if (element === top) {
            return null
        }
    }
    return element
}

module.exports = util
