raw_stats_manager = None


class RawStatsManager(object):

    @staticmethod
    def from_json(json_payload):
        """
        :type json_payload: dict
        :rtype RawStats
        """
        r = RawStats()
        r.assists = json_payload.get('assists', 0)
        r.barracks_killed = json_payload.get('barracksKilled', 0)
        r.bounty_level = json_payload.get('bountyLevel', 0)
        r.champions_killed = json_payload.get('championsKilled', 0)
        r.combat_player_score = json_payload.get('combatPlayerScore', 0)
        r.consumable_purchased = json_payload.get('consumablesPurchased', 0)
        r.damage_dealt_player = json_payload.get('damageDealtPlayer', 0)
        r.double_kills = json_payload.get('doubleKills', 0)
        r.gold = json_payload.get('gold', 0)
        r.gold_earned = json_payload.get('goldEarned', 0)
        r.gold_spent = json_payload.get('goldSpent', 0)
        r.item0 = json_payload.get('item0', 0)
        r.item1 = json_payload.get('item1', 0)
        r.item2 = json_payload.get('item2', 0)
        r.item3 = json_payload.get('item3', 0)
        r.item4 = json_payload.get('item4', 0)
        r.item5 = json_payload.get('item5', 0)
        r.item6 = json_payload.get('item6', 0)
        r.items_purchased = json_payload.get('itemsPurchased', 0)
        r.killing_sprees = json_payload.get('killingSprees', 0)
        r.largest_critical_strike = json_payload.get('largestCriticalStrike', 0)
        r.largest_killing_spree = json_payload.get('largestKillingSpree', 0)
        r.largest_multi_kill = json_payload.get('largestMultiKill', 0)
        r.legendary_items_created = json_payload.get('legendaryItemsCreated', 0)
        r.level = json_payload.get('level', 0)
        r.magic_damage_dealt_player = json_payload.get('magicDamageDealtPlayer', 0)
        r.magic_damage_dealt_to_champions = json_payload.get('magicDamageDealtToChampions', 0)
        r.magic_damage_taken = json_payload.get('magicDamageTaken', 0)
        r.minions_denied = json_payload.get('minionsDenied', 0)
        r.minions_killed = json_payload.get('minionsKilled', 0)
        r.neutral_minions_killed = json_payload.get('neutralMinionsKilled', 0)
        r.neutral_minions_killed_enemy_jungle = json_payload.get('neutralMinionsKilledEnemyJungle', 0)
        r.neutral_minions_killed_your_jungle = json_payload.get('neutralMinionsKilledYourJungle', 0)
        r.nexus_killed = json_payload.get('nexusKilled', False)
        r.node_capture = json_payload.get('nodeCapture', 0)
        r.node_capture_assist = json_payload.get('nodeCaptureAssist', 0)
        r.node_neutralize = json_payload.get('nodeNeutralize', 0)
        r.node_neutralize_assist = json_payload.get('nodeNeutralizeAssist', 0)
        r.num_deaths = json_payload.get('numDeaths', 0)
        r.num_items_bought = json_payload.get('numItemsBought', 0)
        r.objective_player_score = json_payload.get('objectivePlayerScore', 0)
        r.penta_kills = json_payload.get('pentaKills', 0)
        r.physical_damage_dealt_player = json_payload.get('physicalDamageDealtPlayer', 0)
        r.physical_damage_dealt_to_champions = json_payload.get('physicalDamageDealtToChampions', 0)
        r.physical_damage_taken = json_payload.get('physicalDamageTaken', 0)
        r.player_position = json_payload.get('playerPosition', 0)
        r.player_role = json_payload.get('playerRole', 0)
        r.quadra_kills = json_payload.get('quadraKills', 0)
        r.sight_wards_bought = json_payload.get('sightWardsBought', 0)
        r.spell1_cast = json_payload.get('spell1Cast', 0)
        r.spell2_cast = json_payload.get('spell2Cast', 0)
        r.spell3_cast = json_payload.get('spell3Cast', 0)
        r.spell4_cast = json_payload.get('spell4Cast', 0)
        r.summon_spell1_cast = json_payload.get('summonSpell1Cast', 0)
        r.summon_spell2_cast = json_payload.get('summonSpell2Cast', 0)
        r.super_monster_killed = json_payload.get('superMonsterKilled', 0)
        r.team = json_payload.get('team', 0)
        r.team_objective = json_payload.get('teamObjective', 0)
        r.time_played = json_payload.get('timePlayed', 0)
        r.total_damage_dealt = json_payload.get('totalDamageDealt', 0)
        r.total_damage_dealt_to_champions = json_payload.get('totalDamageDealtToChampions', 0)
        r.total_damage_taken = json_payload.get('totalDamageTaken', 0)
        r.total_heal = json_payload.get('totalHeal', 0)
        r.total_player_score = json_payload.get('totalPlayerScore', 0)
        r.total_score_rank = json_payload.get('totalScoreRank', 0)
        r.total_time_crowd_control_dealt = json_payload.get('totalTimeCrowdControlDealt', 0)
        r.total_units_healed = json_payload.get('totalUnitsHealed', 0)
        r.triple_kills = json_payload.get('tripleKills', 0)
        r.true_damage_dealt_player = json_payload.get('trueDamageDealtPlayer', 0)
        r.true_damage_dealt_to_champions = json_payload.get('trueDamageDealtToChampions', 0)
        r.true_damage_taken = json_payload.get('trueDamageTaken', 0)
        r.turrets_killed = json_payload.get('turretsKilled', 0)
        r.unreal_kills = json_payload.get('unrealKills', 0)
        r.victory_point_total = json_payload.get('victoryPointTotal', 0)
        r.vision_wards_bought = json_payload.get('visionWardsBought', 0)
        r.ward_killed = json_payload.get('wardKilled', 0)
        r.ward_placed = json_payload.get('wardPlaced', 0)
        r.win = json_payload.get('win', False)
        return r


def get_raw_stats_manager():
    global raw_stats_manager
    if raw_stats_manager is None:
        raw_stats_manager = RawStatsManager()
    return raw_stats_manager


class RawStats(object):
    """
    Raw Stats DTO
    """
    assists = None
    barracks_killed = None
    bounty_level = None
    champions_killed = None
    combat_player_score = None
    consumable_purchased = None
    damage_dealt_player = None
    double_kills = None
    first_blood = None
    gold = None
    gold_earned = None
    gold_spent = None
    item0 = None
    item1 = None
    item2 = None
    item3 = None
    item4 = None
    item5 = None
    item6 = None
    items_purchased = None
    killing_sprees = None
    largest_critical_strike = None
    largest_killing_spree = None
    largest_multi_kill = None
    legendary_items_created = None
    level = None
    magic_damage_dealt_player = None
    magic_damage_dealt_to_champions = None
    magic_damage_taken = None
    minions_denied = None
    minions_killed = None
    neutral_minions_killed = None
    neutral_minions_killed_enemy_jungle = None
    neutral_minions_killed_your_jungle = None
    nexus_killed = None
    node_capture = None
    node_capture_assist = None
    node_neutralize = None
    node_neutralize_assist = None
    num_deaths = None
    num_items_bought = None
    objective_player_score = None
    penta_kills = None
    physical_damage_dealt_player = None
    physical_damage_dealt_to_champions = None
    physical_damage_taken = None
    player_position = None
    player_role = None
    quadra_kills = None
    sight_wards_bought = None
    spell1_cast = None
    spell2_cast = None
    spell3_cast = None
    spell4_cast = None
    summon_spell1_cast = None
    summon_spell2_cast = None
    super_monster_killed = None
    team = None
    team_objective = None
    time_played = None
    total_damage_dealt = None
    total_damage_dealt_to_champions = None
    total_damage_taken = None
    total_heal = None
    total_player_score = None
    total_score_rank = None
    total_time_crowd_control_dealt = None
    total_units_healed = None
    triple_kills = None
    true_damage_dealt_player = None
    true_damage_dealt_to_champions = None
    true_damage_taken = None
    turrets_killed = None
    unreal_kills = None
    victory_point_total = None
    vision_wards_bought = None
    ward_killed = None
    ward_placed = None
    win = None
