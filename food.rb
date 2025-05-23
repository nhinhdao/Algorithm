#!/usr/bin/env ruby
# interactive_main.rb
#
# How to run:
#   1. Ensure Ruby is installed by running `ruby -v` in your terminal.
#   2. Save this file as interactive_main.rb.
#   3. Run the file using the command: `ruby interactive_main.rb`
#
# Description:
#   This interactive CLI program lets you choose an animal (Cat or Dog),
#   select a food item to feed it, and then watch the animal's reaction
#   (sound printed to the CLI). The program loops until you choose to exit.

# === Food Classes ===
class CatFood; end
class DogFood; end
class HumanFood; end
class Lemon; end
class Milk; end
# Chicken is treated as a food item.
class Chicken; end

# === Animal Classes ===
class Cat
  def initialize
    # A cat likes CatFood, Chicken, and Milk.
    @likes = [CatFood, Chicken, Milk]
  end

  def meow
    puts "meow"
  end

  def eat(food)
    if likes?(food)
      3.times { meow }
    else
      meow
    end
  end

  private

  def likes?(food)
    @likes.include?(food.class)
  end
end

class Dog
  def initialize
    # A dog likes DogFood, CatFood, Chicken, and HumanFood.
    @likes = [DogFood, CatFood, Chicken, HumanFood]
  end

  def bark
    puts "bark"
  end

  def eat(food)
    if likes?(food)
      3.times { bark }
    else
      bark
    end
  end

  private

  def likes?(food)
    @likes.include?(food.class)
  end
end

# === Helper Methods to Create Objects Based on User Input ===

def create_food(choice)
  case choice
  when '1'
    CatFood.new
  when '2'
    DogFood.new
  when '3'
    HumanFood.new
  when '4'
    Lemon.new
  when '5'
    Milk.new
  when '6'
    Chicken.new
  else
    nil
  end
end

def food_name(choice)
  case choice
  when '1'
    "CatFood"
  when '2'
    "DogFood"
  when '3'
    "HumanFood"
  when '4'
    "Lemon"
  when '5'
    "Milk"
  when '6'
    "Chicken"
  else
    "Unknown"
  end
end

def create_animal(choice)
  case choice
  when '1'
    Cat.new
  when '2'
    Dog.new
  else
    nil
  end
end

def animal_type(choice)
  case choice
  when '1'
    "Cat"
  when '2'
    "Dog"
  else
    "Unknown"
  end
end

# === Interactive Menu ===

def interactive_menu
  loop do
    puts "\n--- Animal Feeding Simulation ---"
    puts "Select an animal:"
    puts "1. Cat"
    puts "2. Dog"
    puts "3. Exit"
    print "Enter your choice: "
    animal_choice = gets.chomp
    break if animal_choice == '3'

    animal = create_animal(animal_choice)
    if animal.nil?
      puts "Invalid animal choice. Please try again."
      next
    end

    loop do
      puts "\nSelect a food to feed the #{animal_type(animal_choice)}:"
      puts "1. CatFood"
      puts "2. DogFood"
      puts "3. HumanFood"
      puts "4. Lemon"
      puts "5. Milk"
      puts "6. Chicken"
      print "Enter your choice: "
      if gets.chomp.to_i > 6
        puts "Invalid food choice. Please try again."
        next
      else
        break
      end
    end
    food_choice = gets.chomp
    food = create_food(food_choice)

    puts "\nFeeding #{animal_type(animal_choice)} with #{food_name(food_choice)}..."
    animal.eat(food)
  end
  puts "Exiting simulation. Goodbye!"
end

interactive_menu