class AddRandomStringToUser < ActiveRecord::Migration[5.1]
  def change
    add_column :users, :random_string, :string
  end
end
