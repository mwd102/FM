from .goalkeeper_defend import calculate_goalkeeper_defend
from .sweeper_keeper_defend import calculate_sweeper_keeper_defend
from .sweeper_keeper_support import calculate_sweeper_keeper_support
from .sweeper_keeper_attack import calculate_sweeper_keeper_attack
from .ball_playing_defender_defend import calculate_ball_playing_defender_defend
from .ball_playing_defender_stopper import calculate_ball_playing_defender_stopper
from .ball_playing_defender_cover import calculate_ball_playing_defender_cover
from .central_defender_defend import calculate_central_defender_defend
from .central_defender_stopper import calculate_central_defender_stopper
from .central_defender_cover import calculate_central_defender_cover
from .complete_wing_back_support import calculate_complete_wing_back_support
from .complete_wing_back_attack import calculate_complete_wing_back_attack
from .full_back_defend import calculate_full_back_defend
from .full_back_support import calculate_full_back_support
from .full_back_attack import calculate_full_back_attack
from .inverted_full_back_defend import calculate_inverted_full_back_defend
from .inverted_wing_back_defend import calculate_inverted_wing_back_defend
from .inverted_wing_back_support import calculate_inverted_wing_back_support
from .inverted_wing_back_attack import calculate_inverted_wing_back_attack
from .libero_defend import calculate_libero_defend
from .libero_support import calculate_libero_support
from .nononsense_centre_back_defend import calculate_nononsense_centre_back_defend
from .nononsense_centre_back_stopper import calculate_nononsense_centre_back_stopper
from .nononsense_centre_back_cover import calculate_nononsense_centre_back_cover
from .nononsense_full_back_defend import calculate_nononsense_full_back_defend
from .wide_centre_back_defend import calculate_wide_centre_back_defend
from .wide_centre_back_support import calculate_wide_centre_back_support
from .wide_centre_back_attack import calculate_wide_centre_back_attack
from .wing_back_defend import calculate_wing_back_defend
from .wing_back_support import calculate_wing_back_support
from .wing_back_attack import calculate_wing_back_attack
from .advanced_playmaker_support import calculate_advanced_playmaker_support
from .advanced_playmaker_attack import calculate_advanced_playmaker_attack
from .anchor_defend import calculate_anchor_defend
from .attacking_midfielder_support import calculate_attacking_midfielder_support
from .attacking_midfielder_attack import calculate_attacking_midfielder_attack
from .ball_winning_midfielder_defend import calculate_ball_winning_midfielder_defend
from .ball_winning_midfielder_support import calculate_ball_winning_midfielder_support
from .box_to_box_midfielder_support import calculate_box_to_box_midfielder_support
from .carrilero_support import calculate_carrilero_support
from .central_midfielder_defend import calculate_central_midfielder_defend
from .central_midfielder_support import calculate_central_midfielder_support
from .central_midfielder_attack import calculate_central_midfielder_attack
from .deep_lying_playmaker_defend import calculate_deep_lying_playmaker_defend
from .deep_lying_playmaker_support import calculate_deep_lying_playmaker_support
from .defensive_midfielder_defend import calculate_defensive_midfielder_defend
from .defensive_midfielder_support import calculate_defensive_midfielder_support
from .defensive_winger_defend import calculate_defensive_winger_defend
from .defensive_winger_support import calculate_defensive_winger_support
from .enganche_support import calculate_enganche_support
from .half_back_defend import calculate_half_back_defend
from .inside_forward_support import calculate_inside_forward_support
from .inside_forward_attack import calculate_inside_forward_attack
from .inverted_winger_support import calculate_inverted_winger_support
from .inverted_winger_attack import calculate_inverted_winger_attack
from .mezzala_support import calculate_mezzala_support
from .mezzala_attack import calculate_mezzala_attack
from .raumdeuter_attack import calculate_raumdeuter_attack
from .regista_support import calculate_regista_support
from .roaming_playmaker_support import calculate_roaming_playmaker_support
from .segundo_volante_support import calculate_segundo_volante_support
from .segundo_volante_attack import calculate_segundo_volante_attack
from .shadow_striker_attack import calculate_shadow_striker_attack
from .wide_midfielder_defend import calculate_wide_midfielder_defend
from .wide_midfielder_support import calculate_wide_midfielder_support
from .wide_midfielder_attack import calculate_wide_midfielder_attack
from .wide_playmaker_support import calculate_wide_playmaker_support
from .wide_playmaker_attack import calculate_wide_playmaker_attack
from .wide_target_forward_support import calculate_wide_target_forward_support
from .wide_target_forward_attack import calculate_wide_target_forward_attack
from .winger_support import calculate_winger_support
from .winger_attack import calculate_winger_attack
from .advanced_forward_attack import calculate_advanced_forward_attack
from .complete_forward_support import calculate_complete_forward_support
from .complete_forward_attack import calculate_complete_forward_attack
from .deep_lying_forward_support import calculate_deep_lying_forward_support
from .deep_lying_forward_attack import calculate_deep_lying_forward_attack
from .false_nine_support import calculate_false_nine_support
from .poacher_attack import calculate_poacher_attack
from .pressing_forward_defend import calculate_pressing_forward_defend
from .pressing_forward_support import calculate_pressing_forward_support
from .pressing_forward_attack import calculate_pressing_forward_attack
from .target_forward_support import calculate_target_forward_support
from .target_forward_attack import calculate_target_forward_attack
from .trequartista_attack import calculate_trequartista_attack
from .speed_workrate_score import calculate_speed_workrate_score

__all__ = [
    'calculate_goalkeeper_defend',
    'calculate_sweeper_keeper_defend',
    'calculate_sweeper_keeper_support',
    'calculate_sweeper_keeper_attack',
    'calculate_ball_playing_defender_defend',
    'calculate_ball_playing_defender_stopper',
    'calculate_ball_playing_defender_cover',
    'calculate_central_defender_defend',
    'calculate_central_defender_stopper',
    'calculate_central_defender_cover',
    'calculate_complete_wing_back_support',
    'calculate_complete_wing_back_attack',
    'calculate_full_back_defend',
    'calculate_full_back_support',
    'calculate_full_back_attack',
    'calculate_inverted_full_back_defend',
    'calculate_inverted_wing_back_defend',
    'calculate_inverted_wing_back_support',
    'calculate_inverted_wing_back_attack',
    'calculate_libero_defend',
    'calculate_libero_support',
    'calculate_nononsense_centre_back_defend',
    'calculate_nononsense_centre_back_stopper',
    'calculate_nononsense_centre_back_cover',
    'calculate_nononsense_full_back_defend',
    'calculate_wide_centre_back_defend',
    'calculate_wide_centre_back_support',
    'calculate_wide_centre_back_attack',
    'calculate_wing_back_defend',
    'calculate_wing_back_support',
    'calculate_wing_back_attack',
    'calculate_advanced_playmaker_support',
    'calculate_advanced_playmaker_attack',
    'calculate_anchor_defend',
    'calculate_attacking_midfielder_support',
    'calculate_attacking_midfielder_attack',
    'calculate_ball_winning_midfielder_defend',
    'calculate_ball_winning_midfielder_support',
    'calculate_box_to_box_midfielder_support',
    'calculate_carrilero_support',
    'calculate_central_midfielder_defend',
    'calculate_central_midfielder_support',
    'calculate_central_midfielder_attack',
    'calculate_deep_lying_playmaker_defend',
    'calculate_deep_lying_playmaker_support',
    'calculate_defensive_midfielder_defend',
    'calculate_defensive_midfielder_support',
    'calculate_defensive_winger_defend',
    'calculate_defensive_winger_support',
    'calculate_enganche_support',
    'calculate_half_back_defend',
    'calculate_inside_forward_support',
    'calculate_inside_forward_attack',
    'calculate_inverted_winger_support',
    'calculate_inverted_winger_attack',
    'calculate_mezzala_support',
    'calculate_mezzala_attack',
    'calculate_raumdeuter_attack',
    'calculate_regista_support',
    'calculate_roaming_playmaker_support',
    'calculate_segundo_volante_support',
    'calculate_segundo_volante_attack',
    'calculate_shadow_striker_attack',
    'calculate_wide_midfielder_defend',
    'calculate_wide_midfielder_support',
    'calculate_wide_midfielder_attack',
    'calculate_wide_playmaker_support',
    'calculate_wide_playmaker_attack',
    'calculate_wide_target_forward_support',
    'calculate_wide_target_forward_attack',
    'calculate_winger_support',
    'calculate_winger_attack',
    'calculate_advanced_forward_attack',
    'calculate_complete_forward_support',
    'calculate_complete_forward_attack',
    'calculate_deep_lying_forward_support',
    'calculate_deep_lying_forward_attack',
    'calculate_false_nine_support',
    'calculate_poacher_attack',
    'calculate_pressing_forward_defend',
    'calculate_pressing_forward_support',
    'calculate_pressing_forward_attack',
    'calculate_target_forward_support',
    'calculate_target_forward_attack',
    'calculate_trequartista_attack',
    'calculate_speed_workrate_score'
]
