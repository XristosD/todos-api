# app/controllers/authentication_controller.rb
require 'securerandom'
class AuthenticationController < ApplicationController
    skip_before_action :authorize_request, only: :authenticate
    
    def authenticate
      auth_token = AuthenticateUser.new(auth_params[:email], auth_params[:password]).call
      json_response(auth_token: auth_token)
    end

    def logout
      current_user.update(random_string: SecureRandom.urlsafe_base64(6))
      json_response(message: "Loged out")
    end
  
    private
  
    def auth_params
      params.permit(:email, :password)
    end
  end