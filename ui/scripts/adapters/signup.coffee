FormAdapter = require('./form')
UserModel = require('../models/user')
FormView = require('../views/components/form')
FormLayoutView = require('../views/layouts/form')

# TODO: move copy to content directory

class SignupAdapter extends FormAdapter
    url: '/signup'
    title: 'Sign Up'

    render: ->
        return if @requireLogout()
        super
        @model = new UserModel()
        @view = new FormLayoutView({
            id: 'signup'
            className: 'col-6'
            region: @page
        })
        @view.render({
            title: 'Sign Up for Sagefy'
            description: '''
                Already have an account?
                <a href="/login"><i class="fa fa-sign-in"></i> Login</a>.
                <br />
                By signing up,
                you agree to our <a href="/terms">Terms of Service</a>.
            '''
        })
        @form = new FormView({
            schema: @getSchema()
            region: @view.form
        })
        @form.render()
        @bindEvents()

    bindEvents: ->
        super
        @listenTo(@model, 'sync', @toDashboard.bind(this))

    getSchema: ->
        return @addModelSchema([{
            name: 'name'
            title: 'Username'
            placeholder: 'ex: Unicorn'
        }, {
            name: 'email'
            title: 'Email'
            description: 'We need your email to send notices ' +
                         '<br />and reset password.'
            placeholder: 'ex: unicorn@example.com'
        }, {
            name: 'password'
            title: 'Password'
        }, {
            name: 'submit'
            title: 'Sign Up'
            type: 'submit'
            icon: 'user'
        }])

    toDashboard: ->
        # Hard redirect to get the cookie
        window.location = '/dashboard'

module.exports = SignupAdapter
