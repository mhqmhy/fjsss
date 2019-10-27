var None = 0, ThreeStraights = 1, ThreeFlushes = 2, SixPairs = 3, Dragon = 4;
var special_names = [
  'None', 'Three Straights', 'Three Flushes', 'Six Pairs', 'Dragon'
];
var special_points = [0, 6, 6, 6, 13];
var Front = 0, Center = 1, Back = 2;
var Two = 0, Three = 1, Four = 2, Five = 3, Six = 4, Seven = 5, Eight = 6,
    Nine = 7, Ten = 8, Jack = 9, Queen = 10, King = 11, Ace = 12;
var rank_names = [
  '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ];
var suit_names=['$','&','*','#'];

function suit(card) { return Math.floor(card / 13); }
function rank(card) { return card % 13; }
function map(num){return suit_names[suit(num)]+rank_names[rank(num)];}
class SpecialPattern {
  constructor(hand) {
    var hand_copy = hand.slice(0);
    if (this.dragon(hand_copy)) this.special = Dragon;
    else if (this.six_pairs(hand_copy)) this.special = SixPairs;
    else if (this.three_flushes(hand_copy)) this.special = ThreeFlushes;
    else if (this.three_straights(hand_copy)) this.special = ThreeStraights;
    else this.special = None;
  }

  get pattern() { return this.special; }
  get cards() { return this.hand; }

  is_straight(cards) {
    for (var i = 0; i < cards.length - 1; ++i)
      if (rank(cards[i]) + 1 != rank(cards[i + 1])) return false;
    return true;
  }

  dragon(hand) {
    hand.sort((a, b) => rank(a) - rank(b));
    if (this.is_straight(hand)) {
      this.hand = hand;
      return true;
    }
    return false;
  }

  six_pairs(hand) {
    hand.sort((a, b) => rank(a) - rank(b));
    var num_pairs = 0;
    for (var i = 0; i < 12; ++i) {
      if (rank(hand[i]) == rank(hand[i + 1])) {
        ++num_pairs;
        i += 1;
      }
    }
    if (num_pairs == 6) {
      this.hand = hand;
      return true;
    }
    return false;
  }

  is_flush(cards) {
    for (var i = 0; i < cards.length - 1; ++i)
      if (suit(cards[i]) != suit(cards[i + 1])) return false;
    return true;
  }

  three_flushes(hand) {
    hand.sort((a, b) => suit(a) - suit(b));
    if (this.is_flush(hand.slice(0,3)) && this.is_flush(hand.slice(3,8)) &&
        this.is_flush(hand.slice(8,13))) {
      this.hand = hand;
      return true;
    }
    if (this.is_flush(hand.slice(0,5)) && this.is_flush(hand.slice(5,8)) &&
        this.is_flush(hand.slice(8,13))) {
      this.hand = hand.slice(5,8).concat(hand.slice(0,5), hand.slice(8,13));
      return true;
    }
    if (this.is_flush(hand.slice(0,5)) && this.is_flush(hand.slice(5,10)) &&
        this.is_flush(hand.slice(10,13))) {
      this.hand = hand.slice(10,13).concat(hand.slice(0,5), hand.slice(5,10));
      return true;
    }
    return false;
  }

  remove_straight(buckets, length) {
    for (var i = 0; i < buckets.length; ++i)
      if (buckets[i].length != 0) break;
    for (var j = 1; j < length; ++j)
      if (i + j >= buckets.length || buckets[i + j].length == 0) return [];
    var wave = [];
    for (var j = 0; j < length; ++j)
      wave.push(buckets[i + j].pop());
    return wave;
  }

  three_straights_with_buckets(hand, num_rotated_aces) {
    var buckets = compute_rank_buckets(hand, num_rotated_aces);
    var front = this.remove_straight(buckets, 3);
    var center = this.remove_straight(buckets, 5);
    var back = this.remove_straight(buckets, 5);
    if (front.length && center.length && back.length) {
      this.hand = [].concat(front, center, back);
      return true;
    }
    // Recompute rank buckets since it may be destroyed.
    buckets = compute_rank_buckets(hand, num_rotated_aces);
    center = this.remove_straight(buckets, 5);
    front = this.remove_straight(buckets, 3);
    back = this.remove_straight(buckets, 5);
    if (front.length && center.length && back.length) {
      this.hand = [].concat(front, center, back);
      return true;
    }
    // Recompute rank buckets since it may be destroyed.
    buckets = compute_rank_buckets(hand, num_rotated_aces);
    center = this.remove_straight(buckets, 5);
    back = this.remove_straight(buckets, 5);
    front = this.remove_straight(buckets, 3);
    if (front.length && center.length && back.length) {
      this.hand = [].concat(front, center, back);
      return true;
    }
    return false;
  }

  three_straights(hand) {
    if (this.three_straights_with_buckets(hand, 0)) return true;

    var buckets = compute_rank_buckets(hand, 0);
    var num_aces = buckets[Ace].length;
    if (num_aces == 0) return false;

    for (var i = 0; i < num_aces; ++i) {
      if (this.three_straights_with_buckets(hand, i+1)) return true;
    }
    return false;
  }
};

function compute_rank_buckets(cards, num_rotated_aces) {
  var buckets = [[],[],[],[],[],[],[],[],[],[],[],[],[]];
  for (var card of cards) {
    buckets[rank(card)].push(card);
  }
  if (num_rotated_aces > 0) {
    // Shift the buckets to the right and convert Aces to Ones.
    buckets.unshift([]);
    for (var i = 0; i < num_rotated_aces; ++i)
      buckets[0].push(buckets[13].pop());
  }
  return buckets;
}

function random(end) { return Math.floor(Math.random() * end); }
function random_suit() { return random(4); }

function random_dragon() {
  var ranks = [...Array(13).keys()];
  return ranks.map((rank) => rank + random_suit() * 13);
}

function random_six_pairs() {
  var hand = [];
  var ranks = [...Array(13).keys()];
  shuffle(ranks);
  for (var rank of ranks.slice(0, 7)) {
    var suit = random_suit();
    hand.push(rank + suit * 13);
    suit = (suit + 1) % 4;
    hand.push(rank + suit * 13);
  }
  return hand.slice(0, 13);
}

function random_three_flushes() {
  var hand = [];
  var ranks = [...Array(13).keys()];
  shuffle(ranks);
  var suit = random_suit();
  hand = hand.concat(ranks.slice(0, 3).map((rank) => rank + suit * 13));
  shuffle(ranks);
  suit = (suit + 1) % 4;
  hand = hand.concat(ranks.slice(0, 5).map((rank) => rank + suit * 13));
  shuffle(ranks);
  suit = (suit + 1) % 4;
  hand = hand.concat(ranks.slice(0, 5).map((rank) => rank + suit * 13));
  return hand;
}

function random_three_straights() {
  var deck = [...Array(52).keys()];
  shuffle(deck);

  do {
    // With two Aces and two Ones, no guarantee for three random straights.
    var buckets = compute_rank_buckets(deck, 2);
    var hand = [];
    var pos = random(buckets.length - 3 + 1);
    for (var i = pos; i < pos + 3; ++i)
      if (buckets[i].length) hand.push(buckets[i].pop());
    var pos = random(buckets.length - 5 + 1);
    for (var i = pos; i < pos + 5; ++i)
      if (buckets[i].length) hand.push(buckets[i].pop());
    var pos = random(buckets.length - 5 + 1);
    for (var i = pos; i < pos + 5; ++i)
      if (buckets[i].length) hand.push(buckets[i].pop());
  } while (hand.length < 13);
  return hand;
}

function test_special_patterns() {
  var num_failures = 0;
  for (var i = 0; i < 1000; ++i) {
    var hand = random_dragon();
    var special = new SpecialPattern(hand);
    if (special.pattern < Dragon) {
      console.log('Mistake Dragon as ' + special_names[special.pattern]);
      ++num_failures;
    }

    var hand = random_six_pairs();
    var special = new SpecialPattern(hand);
    if (special.pattern < SixPairs) {
      console.log('Mistake Six Pairs as ' + special_names[special.pattern]);
      ++num_failures;
    }

    var hand = random_three_flushes();
    var special = new SpecialPattern(hand);
    if (special.pattern < ThreeFlushes) {
      console.log('Mistake Three Flushes as ' + special_names[special.pattern]);
      ++num_failures;
    }

    var hand = random_three_straights();
    var special = new SpecialPattern(hand);
    if (special.pattern < ThreeStraights) {
      console.log('Mistake Three Straights as ' + special_names[special.pattern]);
      ++num_failures;
    }
  }
  if (num_failures == 0) console.log('Passed');
}

//-----------------------------------------------------------------------------------
var Junk = 0, Pair = 1, TwoPairs = 2, Continuous=3 ,Triple = 4, Straight = 5, Flush = 6,
    FullHouse = 7, Quadruple = 8, StraightFlush = 9, RoyalFlush = 10;
var pattern_names = [
  'junk', 'pair', 'two pairs', ,'continuous','triple', 'straight', 'flush',
  'full house', 'quadruple', 'straight flush', 'royal flush'
];
var pattern_points = [
  //           Tr       FH Qu SF  RF
  [1, 1, 1, 1, 3, 1, 1, 1, 1,  1,  1],  // front
  [1, 1, 1, 1, 1, 1, 1, 2, 8, 10, 20],  // center
  [1, 1, 1, 1, 1, 1, 1, 1, 4,  5, 10],  // back
];

var junk_value = [
  //2   3   4   5   6   7   8   9   T   J   Q   K   A
  [ 0,  0,  0,  0,  0,  1,  1,  2,  2,  4,  7, 15, 34],
  [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
  [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
];

var junk_value0 = [
  //2   3   4   5   6   7   8   9   T   J   Q   K   A
  [ 0, 20, 20, 21, 21, 22, 23, 24, 26, 30, 34, 42,  0],  //A?
  [ 0,  9,  9, 10, 10, 11, 11, 12, 13, 15, 18,  0,  0],  //K?
  [ 0,  5,  5,  5,  6,  6,  7,  7,  8,  8,  0,  0,  0]   //Q?
];

var one_pair_value = [
  //2   3   4   5   6   7   8   9   T   J   Q   K   A
  [45, 47, 49, 51, 53, 56, 60, 64, 68, 73, 81, 89, 97],
  [ 2,  3,  3,  4,  5,  6,  8, 10, 12, 15, 18, 24, 33],
  [ 0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  2,  2,  3]
];

var one_pair_value0 = [
  //2   3   4   5   6   7   8   9   T   J   Q   K   A
  [96, 96, 96, 96, 96, 96, 97, 97, 97, 97, 98, 98,  0],  //A?
  [86, 86, 86, 86, 86, 87, 87, 88, 89, 89, 90,  0, 91],  //K?
  [76, 76, 77, 77, 77, 78, 78, 78, 79, 80,  0, 82, 83]   //Q?
];

var one_pair_value1 = [
  //2   3   4   5   6   7   8   9   T   J   Q   K   A
  [ 0,  0, 30, 31, 31, 32, 32, 33, 33, 34, 35, 36,  0],  //A?
  [ 0,  0, 23, 23, 23, 23, 23, 24, 25, 25, 26,  0, 27],  //K?
  [ 0,  0, 17, 17, 18, 18, 18, 19, 19, 20,  0, 21, 22]   //Q?
];

var two_pair_value = [
  //2   3   4   5   6   7   8   9   T   J   Q   K   A
  [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
  [ 0, 37, 37, 39, 41, 43, 46, 49, 54, 58, 62, 64, 64],
  [ 0,  3,  3,  4,  4,  5,  7,  8, 10, 11, 13, 14, 14]
];
var continuous_value = [
  //2   3   4   5   6   7   8   9   T   J   Q   K   A
  [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
  [ 0, 37, 37, 39, 41, 43, 46, 49, 54, 58, 62, 64, 64],
  [ 0,  3,  3,  4,  4,  5,  7,  8, 10, 11, 13, 14, 14]
];
var triple_value = [
  //2   3   4   5   6   7   8   9   T   J   Q   K   A
  [99, 99, 99, 99, 99,100,100,100,100,100,100,100,100],
  [63, 66, 69, 71, 72, 72, 74, 74, 74, 75, 75, 75, 76],
  [12, 13, 13, 15, 16, 16, 16, 16, 16, 14, 15, 15, 15]
];

var straight_value = [
  //2   3   4   5   6   7   8   9   T   J   Q   K   A
  [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
  [ 0,  0,  0, 77, 79, 81, 83, 85, 87, 88, 89, 91, 92],
  [ 0,  0,  0, 16, 18, 20, 22, 24, 26, 28, 31, 34, 37]
];

var flush_value = [
  //2   3   4   5   6   7   8   9   T   J   Q   K   A
  [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
  [ 0,  0,  0,  0,  0, 93, 92, 92, 93, 94, 95, 97, 98],
  [ 0,  0,  0,  0,  0, 35, 37, 38, 38, 40, 44, 50, 61]
];

var flush_value2 = [
  //2   3   4   5   6   7   8   9   T   J   Q   K   A
  [ 0,  0,  0,  0, 53, 54, 55, 56, 57, 59, 62, 65,  0],  //A?
  [ 0,  0,  0, 44, 44, 45, 46, 47, 48, 49, 52,  0,  0],  //K?
  [ 0,  0,  0, 41, 41, 41, 42, 42, 44, 45,  0,  0,  0]   //Q?
];

var full_value = [
  //2   3   4   5   6   7   8   9   T   J   Q   K   A
  [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
  [98, 99, 99, 99, 99, 99, 99, 99,100,100,100,100,100],
  [65, 66, 69, 71, 73, 75, 78, 80, 82, 85, 88, 91, 94],
];

var quadruple_value = [
  //2   3   4   5   6   7   8   9   T   J   Q   K   A
  [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
  [100,100,100,100,100,100,100,100,100,100,100,100,100],
  [ 94, 94, 95, 95, 95, 96, 97, 97, 97, 97, 98, 98, 98]
];

class WaveEvaluator {
  constructor(cards, order) {
    this.cards = cards.slice(0);
    this.order = order;

    this.features = [];
    this.extract_features();
    this.win_percent = this.evaluate();
  }

  extract_features() {
    this.cards.sort((a, b) => rank(a) - rank(b));

    var num_junks = 0, num_pairs = 0, num_triples = 0;
    var length = this.cards.length;
    for (var i = 0; i < length; ++i) {
      var r = rank(this.cards[i]);
      if (i + 1 >= length || r != rank(this.cards[i + 1])) {
        this.features.push({type: Junk, rank: r});
        ++num_junks;
      } else if (i + 2 >= length || r != rank(this.cards[i + 2])) {
        this.features.push({type: Pair, rank: r});
        ++num_pairs;
        i += 1;
      } else if (i + 3 >= length || r != rank(this.cards[i + 3])) {
        this.features.push({type: Triple, rank: r});
        ++num_triples;
        i += 2;
      } else {
        this.features.push({type: Quadruple, rank: r});
        i += 3;
      }
    }
    if (num_junks == 5) {
      var high_rank = rank(this.cards[4]);
      var straight = false;
      if (rank(this.cards[0]) + 4 == rank(this.cards[4])) {
        straight = true;
      }
      // Special case for 2345A.

      var flush = true;
      for (var i = 0; i < length - 1; ++i) {
        if (suit(this.cards[i]) != suit(this.cards[i + 1])) {
          flush = false;
          break;
        }
      }

      if (straight && flush) {
        var type = high_rank == Ace ? RoyalFlush : StraightFlush;
        this.features = [{type: type, rank: high_rank}];
      } else if (straight) {
        this.features = [{type: Straight, rank: high_rank}];
      } else if (flush) {
        this.features.pop();
        this.features.push({type: Flush, rank: high_rank});
      }
    }

    this.features.sort((a, b) => a.type == b.type ?
                       b.rank - a.rank : b.type - a.type);

    if (num_pairs == 2) {
      this.features[0].type = TwoPairs;
      if(this.features[0].rank-this.features[1].rank==1){
		this.features[0].type = Continuous; 
	  }
    }
    if (num_triples == 1 && num_pairs == 1) {
      this.features[0].type = FullHouse;
    }
  }

  evaluate() {
    var r0 = this.rank;
    switch (this.pattern) {
      case RoyalFlush:
        return 100;
      case StraightFlush:
        return 100;
      case Quadruple:
        return quadruple_value[this.order][r0];
      case FullHouse:
        return full_value[this.order][r0];
      case Flush:
        var r1 = this.features[1].rank;
        if (this.order == Back && r0 >= Queen)
          return flush_value2[Ace - r0][r1];
        return flush_value[this.order][r0];
      case Straight:
        return straight_value[this.order][r0];
      case Triple:
        return triple_value[this.order][r0];
	  case Continuous:
		return continuous_value[this.order][r0];
      case TwoPairs:
        return two_pair_value[this.order][r0];
      case Pair:
        var r1 = this.features[1].rank;
        if (this.order == Front && r0 >= Queen)
          return one_pair_value0[Ace - r0][r1];
        if (this.order == Center && r0 >= Queen)
          return one_pair_value1[Ace - r0][r1];
        return one_pair_value[this.order][r0];
      case Junk:
        var r1 = this.features[1].rank;
        if (this.order == Front && r0 >= Queen)
          return junk_value0[Ace - r0][r1];
        return junk_value[this.order][r0];
    }
  }

  get pattern() { return this.features[0].type; }
  get rank() { return this.features[0].rank; }
  get value() { return this.win_percent; }
  get points() { return pattern_points[this.order][this.pattern]; }
  get wave() {
    // Special case for 2345A.
    if ((this.pattern == Straight || this.pattern == StraightFlush) &&
        this.rank == Five) {
      return this.cards.slice(4, 5).concat(this.cards.slice(0, 4));
    }
    return this.cards;
  }

  is_smaller_than(wave) {
    var min_features = Math.min(this.features.length, wave.features.length);
    for (var i = 0; i < min_features; ++i) {
      if (this.features[i].type < wave.features[i].type) return true;
      if (this.features[i].type > wave.features[i].type) return false;
      if (this.features[i].rank < wave.features[i].rank) return true;
      if (this.features[i].rank > wave.features[i].rank) return false;
    }
    return false;
  }
};
//----------------------------------------------------------------------------------------

class HandOptimizer {
  constructor(hand, handicap = 0) {
    this.hand = hand.slice(0);
    this.handicap = handicap;

    this.top_waves = [];
    this.optimize_waves();
  }

  optimize_waves() {
    this.hand.sort((a, b) => rank(a) - rank(b));
    this.threshold = 0;
    this.optimize_back();
  }

  optimize_back() {
    for (var b1 = 0; b1 < 9; ++b1) {
      for (var b2 = b1 + 1; b2 < 10; ++b2) {
        for (var b3 = b2 + 1; b3 < 11; ++b3) {
          for (var b4 = b3 + 1; b4 < 12; ++b4) {
            for (var b5 = b4 + 1; b5 < 13; ++b5) {
              this.back = new WaveEvaluator(
                [this.hand[b1], this.hand[b2], this.hand[b3],
                 this.hand[b4], this.hand[b5]], Back);
              if (this.back.pattern == Junk) continue;
              if (200 + this.back.value < this.threshold) continue;

              var bits = (1<<b1) + (1<<b2) + (1<<b3) + (1<<b4) + (1<<b5);
              this.optimize_center(bits);
            }
          }
        }
      }
    }
  }

  optimize_center(bits) {
    out:
    for (var c1 = 0; c1 < 9; ++c1) {
      if ((1 << c1) & bits) continue;
      for (var c2 = c1 + 1; c2 < 10; ++c2) {
        if ((1 << c2) & bits) continue;
        for (var c3 = c2 + 1; c3 < 11; ++c3) {
          if ((1 << c3) & bits) continue;
          for (var c4 = c3 + 1; c4 < 12; ++c4) {
            if ((1 << c4) & bits) continue;
            for (var c5 = c4 + 1; c5 < 13; ++c5) {
              if ((1 << c5) & bits) continue;

              this.center = new WaveEvaluator(
                [this.hand[c1], this.hand[c2], this.hand[c3],
                 this.hand[c4], this.hand[c5]], Center);
              if (this.back.is_smaller_than(this.center)) break out;
              if (100 + this.center.value + this.back.value < this.threshold)
                continue;

              var center_bits = (1<<c1) + (1<<c2) + (1<<c3) + (1<<c4) + (1<<c5);
              this.optimize_front(bits + center_bits);
            }
          }
        }
      }
    }
  }

  optimize_front(bits) {
    out:
    for (var f1 = 0; f1 < 11; ++f1) {
      if ((1 << f1) & bits) continue;
      for (var f2 = f1 + 1; f2 < 12; ++f2) {
        if ((1 << f2) & bits) continue;
        for (var f3 = f2 + 1; f3 < 13; ++f3) {
          if ((1 << f3) & bits) continue;

          this.front = new WaveEvaluator(
            [this.hand[f1], this.hand[f2], this.hand[f3]], Front);
          if (this.center.is_smaller_than(this.front)) break out;

          var sum_value = expected_points(this.front, this.center, this.back);
          var duplicate = false;
          for (var pos = 0; pos < this.top_waves.length; ++pos) {
            if (sum_value < this.top_waves[pos][0]) break;
            if (sum_value == this.top_waves[pos][0]) {
              duplicate = true;
              break;
            }
          }
          if (duplicate) continue;
          if (pos == 0 && this.top_waves.length == this.handicap + 1) continue;

          this.top_waves.splice(pos, 0, [sum_value].concat(
                this.front.wave, this.center.wave, this.back.wave));
          if (this.top_waves.length > this.handicap + 1)
            this.top_waves.shift();
          this.threshold = this.top_waves[0][0];
        }
      }
    }
  }

  get waves() {
    var waves = this.top_waves[0].slice(1);
    return [waves.slice(0, 3), waves.slice(3, 8), waves.slice(8, 13)];
  }

  get points() {
    return this.top_waves[0][0] / 100;
  }
};

function expected_points(front_eval, center_eval, back_eval) {
  var f = front_eval.value / 100.0;
  var c = center_eval.value / 100.0;
  var b = back_eval.value / 100.0;
  var fp = front_eval.points;
  var cp = center_eval.points;
  var bp = back_eval.points;
  var win3 = f*c*b*2*(fp+cp+bp);
  var win2 = f*c*(1-b)*(fp+cp-bp) + f*(1-c)*b*(fp-cp+bp) + (1-f)*c*b*(-fp+cp+bp);
  var win1 = f*(1-c)*(1-b)*(fp-cp-bp) + (1-f)*c*(1-b)*(-fp+cp-bp) +
             (1-f)*(1-c)*b*(-fp-cp+bp);
  var win0 = (1-f)*(1-c)*(1-b)*2*(-fp-cp-bp);
  return Math.floor(100 * (win3 + win2 + win1 + win0));
}
function optimize_hand(hand) {
  var waves = (new HandOptimizer(hand)).waves;
  return waves;
}