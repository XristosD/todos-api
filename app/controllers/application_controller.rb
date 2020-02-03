# app/controllers/application_controller.rb
class ApplicationController < ActionController::API
  include Response
  include ExceptionHandler



  # called before every action on controllers
  before_action :authorize_request
  attr_reader :current_user

  private

  # Check for valid request token and return user
  def authorize_request
    Rails.logger.debug "starting authorizing"
    @current_user = (AuthorizeApiRequest.new(request.headers).call)[:user]
    Rails.logger.debug "stoping authorizing with user #{@current_user}"
  end
end