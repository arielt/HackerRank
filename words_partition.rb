#!/usr/bin/env ruby

# Given a string where in each word letters were randomly shuffled and after
# that words were written without spaces (lets call it X). Also you have a
# dictionary. The task is to return all possible strings S that can be
# transformed into the string X and all words in S are from dictionary.

require 'pp'

def sorts(s)
  s = s.chars.sort.join
end

# recursion
def rec_s(s, start, rv, rvi, xd)
  if s.size == start
    rv[rvi][:fit] = true
    return
  end

  for i in start .. (s.size - 1)
    word = s[start..i]
    sorted = sorts(word)
    if xd.has_key?(sorted)
      rv[rvi][:value] << sorted
      rv << {value: rv[rvi][:value].clone, fit: false}
      rec_s(s, i + 1, rv, rvi, xd)
      rvi = rvi + 1
    end
  end
end

# preparation
def alls(s, dict)
  rv = [value: [], fit: false] # array of records to return
  rvi = 0 # next index in array
  xd = {}
  dict.each do |k,v|
    key = sorts(k)
    if xd.has_key?(key)
      xd[key] << k
    else
      xd[key] = [k]
    end
  end
  rec_s(s, 0, rv, rvi, xd)
  return rv.select {|v| v[:fit]}
end

# driver
dict = {
  "my" => true,
  "car" => true,
  "acr" => true,
  "a" => true,
  "rc" => true
}

s = "ymacr"

puts "String: #{s}"
puts "Dict: #{dict}"
pp alls(s, dict)
